---
id: UNC@20.15.2@MMLCommand@ADD PERFNSE
type: MMLCommand
name: ADD PERFNSE（增加NSE标识）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PERFNSE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能对象管理
status: active
---

# ADD PERFNSE（增加NSE标识）

## 功能

**适用网元：SGSN**

该命令用于增加一个NSE标识，用于Gb接口NSE话统上报的对象。指定NSE NS和指定NSE BSSGP话统测量单元下的指标上报时必需知道所要上报的NSEI，否则无法上报。因此需要通过该命令手动增加动态上报的NSE ID。

## 注意事项

- 该命令执行后立即生效。

- 用户在执行ADD PERFNSE时候必需先使用[**DSP NSE**](../../../Gb接口管理/信令实体管理/显示NSE属性信息（DSP NSE）_26146030.md)查询所有需要处理的NSE标识。
- 本表最大记录数为2048。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [NSE标识（PERFNSE）](configobject/UNC/20.15.2/PERFNSE.md)

## 使用实例

增加一个待处理的NSE标识，NSEI为10：

ADD PERFNSE: NSEI=10 ;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NSE标识(ADD-PERFNSE)_72345789.md`
