(* Define the function d *)
let d n =
  let rec sum_digits n acc =
    if n = 0 then acc
    else sum_digits (n / 10) (acc + (n mod 10))
  in
  n + sum_digits n 0

(* Generate self numbers up to a given limit *)
let generate_self_numbers limit =
  let generated = Array.make limit false in
  for i = 1 to limit - 1 do
    let dn = d i in
    if dn < limit then
      generated.(dn) <- true
  done;
  let self_numbers = ref [] in
  for i = 1 to limit - 1 do
    if not generated.(i) then
      self_numbers := i :: !self_numbers
  done;
  List.rev !self_numbers

(* Main function to write self numbers to a file *)
let () =
  let self_numbers = generate_self_numbers 10000 in
  let oc = open_out "self.out" in
  List.iter (fun number -> Printf.fprintf oc "%d\n" number) self_numbers;
  close_out oc
