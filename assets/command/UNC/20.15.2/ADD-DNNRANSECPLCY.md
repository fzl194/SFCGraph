---
id: UNC@20.15.2@MMLCommand@ADD DNNRANSECPLCY
type: MMLCommand
name: ADD DNNRANSECPLCY（增加DNN RAN侧安全策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DNNRANSECPLCY
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话策略管理
- 5GC用户面安全策略管理
status: active
---

# ADD DNNRANSECPLCY（增加DNN RAN侧安全策略）

## 功能

**适用NF：SMF**

该命令用来增加基于DNN的RAN侧用户面安全策略。策略用于明确是否需要对RAN侧用户面进行完整性保护和加密保护。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 当根据DNN、SST和SD能查询到本配置时，使用本配置的策略，否则使用SET RANSECPLCY中的策略。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| NSIDX | 网络切片索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络切片索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>本参数通过ADD PLMNNS命令进行配置。 |
| UPINTEGRPLCY | 完整性保护策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAN侧用户面完整性保护策略。<br>数据来源：全网规划<br>取值范围：<br>- “SUBFIRST（优先从签约数据获取）”：优先从签约数据获取是否要RAN侧执行用户面保护策略，如果签约不提供该策略，则从本地配置获取。本地配置由参数UPINTEGRTIND和UPCONFIDIND指示。<br>- “LOCAL（从本地配置获取）”：根据本地配置的参数UPINTEGRTIND和UPCONFIDIND来指示RAN侧是否要执行用户面保护策略。<br>默认值：SUBFIRST<br>配置原则：无 |
| UPINTEGRTIND | 本地完整性保护指示 | 可选必选说明：可选参数<br>参数含义：该参数是本地配置，用于指示RAN侧是否要执行用户面完整性保护策略。<br>数据来源：全网规划<br>取值范围：<br>- “REQUIRED（需要）”：RAN侧需要执行该用户面保护。<br>- “PREFERRED（优选）”：RAN侧如果支持该用户面保护，则需要执行。<br>- “NOTNEEDED（不需要）”：RAN侧不需要执行该用户面保护。<br>- “NOTCARRY（不携带）”：本地不携带该用户面保护策略。<br>默认值：PREFERRED<br>配置原则：<br>当“本地完整性保护指示”参数配置为NOTCARRY时，“本地加密保护指示”参数也建议配置为NOTCARRY。如果一个配置为NOTCARRY，另一个不为NOTCARRY时，另一个会被当做NOTCARRY处理。 |
| UPINTEGPDUPLCY | 完整性保护PDU策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定完整性保护指示为“REQUIRED”，但是会话AMBR大于UE支持的完整性保护最大速率时的处理策略。<br>数据来源：全网规划<br>取值范围：<br>- “DONOTHING（不做处理）”：保持会话AMBR大于UE支持的完整性保护最大速率。<br>- “CORRECT（纠正）”：将RAN侧需要执行用户面完整性保护纠正为RAN侧如果支持用户面完整性保护才执行。<br>- “REDUCE（限速）”：将会话AMBR降低至UE支持的完整性保护最大速率。<br>- “REJECT（拒绝）”：拒绝会话建立或者删除会话。<br>默认值：REDUCE<br>配置原则：无 |
| UPCONFIDPLCY | 加密保护策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAN侧用户面加密保护策略。<br>数据来源：全网规划<br>取值范围：<br>- “SUBFIRST（优先从签约数据获取）”：优先从签约数据获取是否要RAN侧执行用户面保护策略，如果签约不提供该策略，则从本地配置获取。本地配置由参数UPINTEGRTIND和UPCONFIDIND指示。<br>- “LOCAL（从本地配置获取）”：根据本地配置的参数UPINTEGRTIND和UPCONFIDIND来指示RAN侧是否要执行用户面保护策略。<br>默认值：SUBFIRST<br>配置原则：无 |
| UPCONFIDIND | 本地加密保护指示 | 可选必选说明：可选参数<br>参数含义：该参数是本地配置，用于指示RAN侧是否要执行用户面加密保护策略。<br>数据来源：全网规划<br>取值范围：<br>- “REQUIRED（需要）”：RAN侧需要执行该用户面保护。<br>- “PREFERRED（优选）”：RAN侧如果支持该用户面保护，则需要执行。<br>- “NOTNEEDED（不需要）”：RAN侧不需要执行该用户面保护。<br>- “NOTCARRY（不携带）”：本地不携带该用户面保护策略。<br>默认值：PREFERRED<br>配置原则：<br>当“本地加密保护指示”参数配置为NOTCARRY时，“本地完整性保护指示”参数也建议配置为NOTCARRY。如果一个配置为NOTCARRY，另一个不为NOTCARRY时，另一个会被当做NOTCARRY处理。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNRANSECPLCY]] · DNN RAN侧安全策略（DNNRANSECPLCY）

## 使用实例

配置基于DNN的RAN侧用户面安全策略参数为签约优先，执行如下命令：

```
ADD DNNRANSECPLCY:DNN="huawei.com",NSIDX=0,UPINTEGRPLCY=SUBFIRST,UPINTEGRTIND=PREFERRED,UPINTEGPDUPLCY=REDUCE,UPCONFIDPLCY=SUBFIRST,UPCONFIDIND=PREFERRED;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DNN-RAN侧安全策略（ADD-DNNRANSECPLCY）_96805377.md`
