---
id: UNC@20.15.2@MMLCommand@ADD IMEIGPMEM
type: MMLCommand
name: ADD IMEIGPMEM（增加IMEI群组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMEIGPMEM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户终端管理
- IMEI群组成员管理
status: active
---

# ADD IMEIGPMEM（增加IMEI群组成员）

## 功能

**适用网元：SGSN、MME**

此命令用于为 [**ADD IMEIGP**](../IMEI群组管理/增加IMEI群组(ADD IMEIGP)_72225435.md) 增加的IMEI群组增加IMEI成员，完成以群粒度进行业务策略控制。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为10000。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指示IMEI群组标识。<br>前提条件：<br>“IMEI群组标识”<br>已经通过<br>[**ADD IMEIGP**](../IMEI群组管理/增加IMEI群组(ADD IMEIGP)_72225435.md)<br>配置。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |
| IMEITAC | IMEI设备型号核准号码 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户的设备型号核准号码（TAC）。TAC由IMEI的前8位数字组成，由欧洲型号认证中心分配，用来标识某一型号的手机。<br>数据来源：本端规划<br>取值范围：8位十进制数<br>默认值：无 |
| UEDESC | 终端详细信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定终端详细信息。<br>数据来源：本端规划<br>取值范围：0~255位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEIGPMEM]] · IMEI群组成员（IMEIGPMEM）

## 使用实例

增加一个IMEI群组，其群组名称为“iphone”，群组成员设备型号核准号码为35437906：

ADD IMEIGP: IMEIGPID=1, IMEIGPN="iphone";

ADD IMEIGPMEM: IMEIGPID=1, IMEITAC="35437906";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IMEIGPMEM.md`
