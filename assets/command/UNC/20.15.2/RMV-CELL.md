---
id: UNC@20.15.2@MMLCommand@RMV CELL
type: MMLCommand
name: RMV CELL（删除小区）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CELL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- 小区管理
status: active
---

# RMV CELL（删除小区）

## 功能

![](删除小区(RMV CELL)_72225669.assets/notice_3.0-zh-cn_2.png)

删除小区将导致基于该小区的所有业务被中断，请谨慎操作。

**适用网元：SGSN**

此命令用于删除指定的小区。

## 注意事项

- 删除小区将导致基于该小区的所有业务被中断，请谨慎操作。
- 删除方式包括：若只输入“NSEI”，则删除该NSE下所有的小区；若同时输入“NSEI”和“BVCI”，则删除NSEI和BVCI唯一确定的小区；若只输入“CELLID”，则删除该CELLID对应的小区。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：此参数用于表示网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |
| BVCI | BVCI | 可选必选说明：可选参数<br>参数含义：此参数用于表示小区的BSSGP虚连接标识。<br>取值范围：0～65535<br>默认值：无 |
| CELLID | 小区号 | 可选必选说明：可选参数<br>参数含义：此参数用于表示小区的标识。CELLID = MCC + MNC + LAC + RAC + CI。<br>取值范围：15~16位十六进制数<br>默认值：无<br>说明：说明：如果输入了小区号，则不允许输入NSE标识或者BVCI。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CELL]] · 小区（CELL）

## 使用实例

删除NSEI为12003，BVCI为1201的小区：

RMV CELL: NSEI=12003, BVCI=1201;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CELL.md`
