use crate::error::RouterError;
use crate::DbPool;
use actix_web::web::{self, ReqData};
use diesel::prelude::*;

/// This will teminate the user token
pub async fn logout(pool: web::Data<DbPool>, data: ReqData<u32>) -> Result<String, RouterError> {
    use crate::models::Token;
    use crate::schema::app_tokens::dsl::*;

    let req_user_id = data.into_inner();

    // String -> Message
    let result = web::block(move || {
        let mut conn = pool.get().unwrap();

        // Get the latest token
        let tokens: Vec<Token> = app_tokens
            .filter(user_id.eq(req_user_id as i32))
            .order(created_at.desc())
            .limit(1)
            .load::<Token>(&mut conn)
            .unwrap();

        // Get THE token
        let Some(token)= tokens.get(0) else {
            return Err(RouterError::NotFound);
        };

        // Now teminate the token
        // Set the terminated to true
        // And set request id to the terminated_by_id
        // This may change.
        diesel::update(token)
            .set((terminated.eq(true), terminated_by_id.eq(req_user_id as i32)))
            .execute(&mut conn)
            .unwrap();

        Ok("Logged Out".to_string())
    })
    .await
    .unwrap()?;

    Ok(result)
}