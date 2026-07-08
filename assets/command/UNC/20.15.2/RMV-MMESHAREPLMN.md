---
id: UNC@20.15.2@MMLCommand@RMV MMESHAREPLMN
type: MMLCommand
name: RMV MMESHAREPLMN（删除MME的共享PLMN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMESHAREPLMN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME POOL区管理
- MME共享管理
status: active
---

# RMV MMESHAREPLMN（删除MME的共享PLMN）

## 功能

**适用网元：MME**

该命令用于删除一条MME的共享PLMN记录。

## 注意事项

- 该命令执行后立即生效。
- 系统支持的PLMN变少。
- 删除后该PLMN网络下的用户会附着，路由更新，网络切换失败。
- 如果待删除记录被**[ADD SHAREPLMNMEM](../../基于区域MME共享管理/共享PLMN群组成员/增加共享PLMN群组成员(ADD SHAREPLMNMEM)_19405129.md)**配置引用，则不能删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定由ITU-T统一分配的移动网络所在国家的标识符。<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个国家内的PLMN标识符。<br>取值范围：位数为2或3的十进制数<br>默认值：无 |

## 操作的配置对象

- [MME的共享PLMN（MMESHAREPLMN）](configobject/UNC/20.15.2/MMESHAREPLMN.md)

## 使用实例

删除一个 “移动国家码” 为 “123” 、 “移动网号” 为 “01” 的MME的共享PLMN：

RMV MMESHAREPLMN: MCC="123", MNC="01";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MME的共享PLMN（RMV-MMESHAREPLMN）_72225765.md`
