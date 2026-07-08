---
id: UNC@20.15.2@MMLCommand@RMV DCNMAP
type: MMLCommand
name: RMV DCNMAP（删除DCN映射关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DCNMAP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN映射关系
status: active
---

# RMV DCNMAP（删除DCN映射关系）

## 功能

**适用网元：MME**

此命令用于删除DCN与UE USAGE TYPE的映射关系。删除后该DCN不再服务于通过 [**ADD DCNMAP**](增加DCN映射关系(ADD DCNMAP)_26305638.md) 配置的UE USAGE TYPE范围内的用户。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定DCN ID。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |
| BGNUEUSAGETYPE | 起始UE USAGE TYPE | 可选必选说明：必选参数<br>参数含义：该参数用于指定起始UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DCNMAP]] · DCN映射关系（DCNMAP）

## 使用实例

删除DCN ID是1的DCN所服务的用户范围：

RMV DCNMAP: DCNID=1, BGNUEUSAGETYPE=150;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DCNMAP.md`
