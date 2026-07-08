---
id: UNC@20.15.2@MMLCommand@RMV HOMEIP
type: MMLCommand
name: RMV HOMEIP（删除Home IP地址）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HOMEIP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- Home IP
status: active
---

# RMV HOMEIP（删除Home IP地址）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于删除Home IP地址配置。

## 注意事项

- 该命令执行后立即生效。

- 该命令不指定HOMEIPID时，表示删除该HOMEGROUPINDX下的所有IP地址记录。
- HOMEIPID不输入时表示删除该组内所有记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMEGROUPINDX | Home Group编号 | 可选必选说明：必选参数<br>参数含义：该参数用来设置Home Group的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| HOMEIPID | Home IP编号 | 可选必选说明：可选参数<br>参数含义：该参数用来设置该Home IP的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HOMEIP]] · Home IP地址（HOMEIP）

## 使用实例

- 删除“Home Group编号”为“1”，“Home IP编号”为“1”的Home IP地址配置：
  ```
  LST HOMEIP: HOMEGROUPINDX=1, HOMEIPID=1;
  ```
- 删除“Home Group编号”为“1”的全部Home IP地址配置：
  ```
  LST HOMEIP: HOMEGROUPINDX=1;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HOMEIP.md`
