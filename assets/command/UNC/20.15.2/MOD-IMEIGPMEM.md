---
id: UNC@20.15.2@MMLCommand@MOD IMEIGPMEM
type: MMLCommand
name: MOD IMEIGPMEM（修改IMEI群组成员）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD IMEIGPMEM（修改IMEI群组成员）

## 功能

**适用网元：SGSN、MME**

此命令用于修改IMEI群组成员记录的终端详细信息。

如果需要将设备型号划分到其他IMEI群组中，需要通过 [**RMV IMEIGPMEM**](删除IMEI群组成员(RMV IMEIGPMEM)_26145760.md) 删除后，再通过 [**ADD IMEIGPMEM**](增加IMEI群组成员(ADD IMEIGPMEM)_26305568.md) 增加。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：待修改的IMEI群组标识。<br>前提条件：<br>“IMEI群组标识”<br>已经通过<br>[**ADD IMEIGP**](../IMEI群组管理/增加IMEI群组(ADD IMEIGP)_72225435.md)<br>配置。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |
| IMEITAC | IMEI设备型号核准号码 | 可选必选说明：必选参数<br>参数含义：待修改用户的设备型号核准号码（TAC）。TAC由IMEI的前8位数字组成，由欧洲型号认证中心分配，用来标识某一型号的手机。<br>数据来源：本端规划<br>取值范围：8位十进制数<br>默认值：无 |
| UEDESC | 终端详细信息 | 可选必选说明：可选参数<br>参数含义：待修改的用户终端详细描述。<br>数据来源：本端规划<br>取值范围：0~255位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEIGPMEM]] · IMEI群组成员（IMEIGPMEM）

## 使用实例

将用户终端详细信息修改为“IPHONE1”：

MOD IMEIGPMEM: IMEIGPID=1, IMEITAC="35437906", UEDESC="IPHONE1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMEI群组成员(MOD-IMEIGPMEM)_72345359.md`
