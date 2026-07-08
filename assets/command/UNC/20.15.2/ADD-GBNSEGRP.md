---
id: UNC@20.15.2@MMLCommand@ADD GBNSEGRP
type: MMLCommand
name: ADD GBNSEGRP（增加NSE和属性模板的关联）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GBNSEGRP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- NSE属性管理
status: active
---

# ADD GBNSEGRP（增加NSE和属性模板的关联）

## 功能

**适用网元：SGSN**

此命令用于增加一组NSE到属性模板的关联，通过属性模板来制定NSE的属性。使用 [**LST GBNSECFGPARA**](../NSE属性模板管理/查询NSE属性模板(LST GBNSECFGPARA)_72345605.md) 命令查询NSE属性模板，与该命令中配置的属性相关联。

此命令只适用于Gb over IP自动配置的场景。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为8192。
- 如果不执行此命令，自动配置的NSE则使用系统默认模板，其“模板索引”值为“0”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPINDEX | 关联索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加关联的索引 。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |
| NSEIBGN | 起始NSEI | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加关联的起始NSEI。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无<br>配置原则：<br>- 起始NSEI不大于结束NSEI。<br>- NSEI范围不能相同，不能包含。 |
| NSEIEND | 结束NSEI | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加关联的结束NSEI。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无<br>配置原则：<br>- 起始NSEI不大于结束NSEI。<br>- 两组NSEI区域之间，不允许存在交集。 |
| PARAINDEX | 关联的NSE属性模板索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加关联的NSE属性模板索引。<br>前提条件：该参数已增加，参见<br>[**ADD GBNSECFGPARA**](../NSE属性模板管理/增加NSE属性模板(ADD GBNSECFGPARA)_26146004.md)<br>。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待增加关联的描述信息。<br>数据来源：整网规划<br>取值范围： 1～33位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBNSEGRP]] · NSE和属性模板的关联（GBNSEGRP）

## 使用实例

增加一组NSE和属性模板的关联， “关联索引” 为 “0” ， “起始NSEI ” 为 “1” ， “结束NSEI ” 为 “3” ， “关联的NSE属性模板索引” 为 “1” ， “描述信息” 为 “DEFAULT” ：

ADD GBNSEGRP: GRPINDEX=0, NSEIBGN=1, NSEIEND=3, PARAINDEX=1, DESC="DEFAULT";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GBNSEGRP.md`
