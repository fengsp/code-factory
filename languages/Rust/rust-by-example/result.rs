mod checked {
    #[deriving(Show)]
    pub enum MathError {
        DivisionByZero,
        NegativeLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // This operation would `fail`, instead let's return the reason of
            // the failure wrapped in `Err`
            Err(DivisionByZero)
        } else {
            // This operation is valid, return the result wrapped in `Ok`
            Ok(x / y)
        }
    }

    pub fn sqrt(x: f64) -> MathResult {
        if x < 0.0 {
            Err(NegativeSquareRoot)
        } else {
            Ok(x.sqrt())
        }
    }

    pub fn ln(x: f64) -> MathResult {
        if x < 0.0 {
            Err(NegativeLogarithm)
        } else {
            Ok(x.ln())
        }
    }
}

fn op(x: f64, y: f64) -> f64 {
    match checked::div(x, y) {
        Err(why) => fail!("{}", why),
        Ok(ratio) => match checked::ln(ratio) {
            Err(why) => fail!("{}", why),
            Ok(ln) => match checked::sqrt(ln) {
                Err(why) => fail!("{}", why),
                Ok(sqrt) => sqrt,
            },
        },
    }
}

fn main() {
    println!("{}", op(1.0, 10.0));
}
