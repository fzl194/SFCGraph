---
id: UNC@20.15.2@MMLCommand@SET SDBTMR
type: MMLCommand
name: SET SDBTMR（设置核查定时器配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SDBTMR
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 用户数据资源核查
status: active
---

# SET SDBTMR（设置核查定时器配置）

## 功能

**适用网元：SGSN、MME**

此命令用于设置系统中SDB（Subscriber DataBase）模块维护相关的定时器配置。

## 注意事项

- 该命令执行后生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PURGTMR | 用户分离后签约数据保留时间（h） | 可选必选说明：必选参数<br>参数含义：该参数用于指定定时器在用户分离后启动，在用户附着后停止，如果超时，将删除<br>UNC<br>上的用户的签约数据。<br>数据来源：整网规划<br>取值范围：0～240h<br>系统初始设置值：24<br>配置原则：建议值为24h。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDBTMR]] · 核查定时器配置（SDBTMR）

## 使用实例

1. 设置系统用户分离后签约数据保留时间：
  SET SDBTMR: PURGTMR=24;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SDBTMR.md`
