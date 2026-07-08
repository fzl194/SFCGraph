---
id: UNC@20.15.2@MMLCommand@ADD TLSSCENE
type: MMLCommand
name: ADD TLSSCENE（增加TLS证书场景）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TLSSCENE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS证书场景管理
status: active
---

# ADD TLSSCENE（增加TLS证书场景）

## 功能

该命令用于添加TLS证书使用场景。

## 注意事项

- 该命令执行后立即生效。

- 若TLSSCENE场景关联的TLSPARA “MODE”为服务端模式，当参数“VERIFYLOCALCERT”设置为“No”时，不校验本端证书，存在安全风险。
- 当[**ADD TLSPARA**](../HTTP TLS安全管理/增加TLS参数（ADD TLSPARA）_84132096.md)命令中参数“HTTP模式”配置为Server时参数“VERIFYLOCALIP”生效，若配置为Client则参数“VERIFYLOCALIP”无实际效果。

- 最多可输入254条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定证书场景的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~254。<br>默认值：无<br>配置原则：无 |
| SCENE | 证书使用场景名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定证书使用场景的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。不支持中文字符。只能由“_”、数字和大小写字母组成。<br>默认值：无<br>配置原则：无 |
| TYPE | 场景类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示证书使用场景类型。<br>数据来源：本端规划<br>取值范围：<br>- “SCENE_CA（CA证书场景类型）”：CA证书场景类型<br>- “SCENE_NE（设备证书场景类型）”：设备证书场景类型<br>默认值：无<br>配置原则：无 |
| DESC | 证书使用场景描述 | 可选必选说明：可选参数<br>参数含义：描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| VERIFYLOCALCERT | 是否验证本端证书 | 可选必选说明：该参数在"TYPE"配置为"SCENE_NE"时为条件可选参数。<br>参数含义：该参数用于指示是否验证本端证书。<br>数据来源：本端规划<br>取值范围：<br>- “Yes（开启校验本端证书）”：开启校验本端证书<br>- “No（关闭校验本端证书）”：关闭校验本端证书<br>默认值：无<br>配置原则：无 |
| VERIFYLOCALIP | 本端IP校验开关 | 可选必选说明：该参数在"VERIFYLOCALCERT"配置为"Yes"时为条件可选参数。<br>参数含义：该参数用于指示服务端在证书更新阶段是否校验本端IP地址。开启本端IP校验后，将校验本端关联证书中的IP地址与HTTPLE配置中的IP地址是否一致，如果不一致则该证书激活失败。<br>数据来源：本端规划<br>取值范围：<br>- “Yes（开启校验本端证书）”：开启校验本端证书<br>- “No（关闭校验本端证书）”：关闭校验本端证书<br>默认值：无<br>配置原则：<br>若客户端开启IP校验，服务端证书IP与实际使用IP不匹配，会导致客户端校验服务端证书失败，业务建链失败。开启该参数可以提前拦截该问题。 |

## 操作的配置对象

- [TLS证书场景（TLSSCENE）](configobject/UNC/20.15.2/TLSSCENE.md)

## 使用实例

若运营商想增加一个TLS证书使用场景，索引是1，场景是CA，可以用如下命令：

```
ADD TLSSCENE:INDEX=1, SCENE="CA", TYPE=SCENE_CA, DESC="CA";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加TLS证书场景（ADD-TLSSCENE）_29213279.md`
