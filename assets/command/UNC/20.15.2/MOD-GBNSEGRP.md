---
id: UNC@20.15.2@MMLCommand@MOD GBNSEGRP
type: MMLCommand
name: MOD GBNSEGRP（修改NSE和属性模板的关联）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GBNSEGRP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- NSE属性管理
status: active
---

# MOD GBNSEGRP（修改NSE和属性模板的关联）

## 功能

**适用网元：SGSN**

此命令用于修改NSE和属性模板的关联，通过属性模板制定NSE的属性。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPINDEX | 关联索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待修改的关联索引 。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |
| NSEIBGN | 起始NSEI | 可选必选说明：可选参数<br>参数含义：该参数用于指定修改后关联的起始NSEI。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |
| NSEIEND | 结束NSEI | 可选必选说明：可选参数<br>参数含义：该参数用于指定修改后关联的结束NSEI。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |
| PARAINDEX | 关联的NSE属性模板索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定修改后关联的NSE属性模板索引。<br>前提条件：该参数已在<br>[**ADD GBNSECFGPARA**](../NSE属性模板管理/增加NSE属性模板(ADD GBNSECFGPARA)_26146004.md)<br>中添加。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定修改后关联的描述信息。<br>数据来源：整网规划<br>取值范围：1～33位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBNSEGRP]] · NSE和属性模板的关联（GBNSEGRP）

## 使用实例

修改一组 “关联索引” 为 “0” 的NSE到属性模板的关联，且 “起始NSEI ” 改为 “2” ， “结束NSEI ” 改为 “5” ：

MOD GBNSEGRP: GRPINDEX=0, NSEIBGN=2, NSEIEND=5;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GBNSEGRP.md`
