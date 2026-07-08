---
id: UNC@20.15.2@MMLCommand@RMV GWSELBYIMEI
type: MMLCommand
name: RMV GWSELBYIMEI（删除基于IMEI选择GGSN/P-GW配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GWSELBYIMEI
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
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- 基于IMEI选择GGSN P-GW
status: active
---

# RMV GWSELBYIMEI（删除基于IMEI选择GGSN/P-GW配置）

## 功能

**适用网元：SGSN、MME**

该命令用于删除基于IMEI选择GGSN/P-GW配置记录。

## 注意事项

- 此命令执行后立即生效。
- 此命令执行后，满足条件的终端在[**ADD GWSELPLCY**](../GGSN_P-GW选择/增加GGSN_P-GW选择策略（ADD GWSELPLCY）_26145944.md)中配置的基于“定制标识类型”选择网关的功能将重新生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指示IMEI群组标识，<br>UNC<br>需要为这些类型终端选择特定GGSN/P-GW。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWSELBYIMEI]] · 基于IMEI选择GGSN/P-GW配置（GWSELBYIMEI）

## 使用实例

假如运营商参考 [**ADD GWSELBYIMEI**](增加基于IMEI选择GGSN_P-GW配置(ADD GWSELBYIMEI)_72345541.md) 的命令使用实例添加了配置记录，同时也参考 [**ADD GWSELPLCY**](../GGSN_P-GW选择/增加GGSN_P-GW选择策略（ADD GWSELPLCY）_26145944.md) 配置了其他的网关选择策略，同时符合这两条配置命令要求的终端将优先根据IMEI选择网关，如果想让这类终端使用 [**ADD GWSELPLCY**](../GGSN_P-GW选择/增加GGSN_P-GW选择策略（ADD GWSELPLCY）_26145944.md) 中配置的网关选择策略，执行如下命令，将基于IMEI选择GGSN/P-GW配置记录删除即可：

RMV GWSELBYIMEI: IMEIGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GWSELBYIMEI.md`
