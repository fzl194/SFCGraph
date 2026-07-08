---
id: UNC@20.15.2@MMLCommand@ADD POOL
type: MMLCommand
name: ADD POOL（增加POOL配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: POOL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL区配置
status: active
---

# ADD POOL（增加POOL配置信息）

## 功能

![](增加POOL配置信息(ADD POOL)_72225781.assets/notice_3.0-zh-cn_2.png)

[**ADD POOL**](增加POOL配置信息(ADD POOL)_72225781.md) 命令执行后需要复位整系统才能生效。

**适用网元：SGSN**

该命令用于增加POOL配置信息。

## 注意事项

- 该命令执行后需要复位整系统才能生效，虚机场景复位整系统请参考**RST NODEBATCH**命令，裸机场景请参考**RST MESYS**命令。
- 该命令最大记录数为1条。
- 融合POOL组网场景下，“NRI长度”不能大于8。
- 当软参“BYTE_EX_B365”BIT4设置为“0”时，对于NB-IoT独立部署的场景，无法添加ADD POOL。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POOL标识。<br>数据来源：整网规划<br>取值范围：0~4095<br>默认值：无 |
| NRILENGTH | NRI长度 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRI的长度，即NRI由几个bit组成。最大的长度为10bits。<br>数据来源：整网规划<br>取值范围：1~10<br>默认值：无<br>配置原则：SGSN支持迁移功能时，允许的POOL NRI最大长度为8<br>说明：- POOL支持的UNC的最大个数是（2n–1）/N向下取整，n为本POOL的“NRI长度”，N为每个UNC规划的NRI个数。<br>- 中国区“NRI长度”只能配置7bits，海外“NRI长度”只能配置5bits。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/POOL]] · POOL配置信息（POOL）

## 使用实例

增加一个POOL配置信息，POOLID为1，NRILENGTH为5：

ADD POOL: POOLID=1, NRILENGTH=5;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加POOL配置信息(ADD-POOL)_72225781.md`
