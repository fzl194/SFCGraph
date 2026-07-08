---
id: UNC@20.15.2@MMLCommand@MOD NSDNN
type: MMLCommand
name: MOD NSDNN（修改网络切片支持的DNN）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NSDNN
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 网络切片内DNN管理
status: active
---

# MOD NSDNN（修改网络切片支持的DNN）

## 功能

**适用NF：SMF**

该命令用于修改指定的网络切片属性。

## 注意事项

- 该命令执行后立即生效。

- 该命令无法用于修改BINDSMFINFOID。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSIDX | 网络切片索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络切片，可以使用LST PLMNNS命令查询获取。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>本参数通过ADD NFNS命令进行配置，且NF类型必须是NfSMF。 |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定的网络切片支持的数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。可配置通配DNN，即“*”，表示支持所有DNN。<br>默认值：无<br>配置原则：<br>确保为S-NSSAI增加其支持的DNN在LST APN中能够查询到。 |
| DEFIWKIND | EPS互操作默认切片指示 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDN连接建立流程中根据DNN为用户分配的互操作默认切片。<br>数据来源：本端规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：<br>5G用户在EPS网络建立PDN连接时，当运营商希望SMF本地根据DNN配置用于N26互操作流程的切片时，需要设置该参数为"YES"。当运营商希望SMF通过UDM获取签约信息分配切片时，可以设置该参数为"NO"。为了避免发生SMF通过UDM获取不到签约的切片的异常场景，强烈建议设置该参数为"YES"。 |
| BINDSMFINFOID | 绑定的SMFINFO ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定的SMFINFOEXT记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>- 默认为空，表示在SmfInfo及SmfInfoList中所有SmfInfo里都携带。<br>- 如果期望仅在SmfInfoList中某个SmfInfo中携带，该参数取值需要与通过与ADD SMFINFOEXT命令配置的SMFINFOID一致。<br>- 如果期望仅在SmfInfo中携带，取值应为“bind_smf_info”时。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSDNN]] · 网络切片支持的DNN（NSDNN）

## 使用实例

将DNN为"huawei.com"的eMBB切片（假设索引为0）修改为EPS互操作默认切片：

```
MOD NSDNN: NSIDX=0, DNN="huawei.com", DEFIWKIND=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改网络切片支持的DNN（MOD-NSDNN）_96242642.md`
