---
id: UNC@20.15.2@MMLCommand@RMV IMEIGPMEM
type: MMLCommand
name: RMV IMEIGPMEM（删除IMEI群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMEIGPMEM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户终端管理
- IMEI群组成员管理
status: active
---

# RMV IMEIGPMEM（删除IMEI群组成员）

## 功能

**适用网元：SGSN、MME**

此命令用于删除IMEI群组成员记录。

## 注意事项

此命令执行后立即生效。

成员删除后，不能再使用群组对应的业务策略。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：待删除的IMEI群组标识。<br>取值范围：1~50<br>默认值：无 |
| IMEITAC | IMEI设备型号核准号码 | 可选必选说明：必选参数<br>参数含义：待删除的用户设备型号核准号码（TAC）。TAC由IMEI的前8位数字组成，由欧洲型号认证中心分配，用来标识某一型号的手机。<br>取值范围：8位十进制数<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEIGPMEM]] · IMEI群组成员（IMEIGPMEM）

## 使用实例

将群标识为1的IMEI群组下，设备型号核准号码为35437906的成员删除：

RMV IMEIGPMEM: IMEIGPID=1, IMEITAC="35437906";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IMEIGPMEM.md`
