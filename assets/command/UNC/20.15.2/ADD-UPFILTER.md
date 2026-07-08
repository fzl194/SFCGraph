---
id: UNC@20.15.2@MMLCommand@ADD UPFILTER
type: MMLCommand
name: ADD UPFILTER（增加UPF过滤组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPFILTER
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP过滤组绑定管理
status: active
---

# ADD UPFILTER（增加UPF过滤组）

## 功能

**适用NF：SMF**

该命令用于为UPF添加一个过滤组，并将过滤组ID、DNN、UP节点这三者进行绑定。

UPF节点在不同的DNN下可以拥有不同的过滤器组，因此过滤组绑定参数必须包含DNN。

通过增加一个过滤组可以使得UPF在侦测到满足该过滤组条件的数据流后可以执行特定的操作，比如丢弃。

过滤组具体的参数可以通过LST FILTERGP查询。

## 注意事项

- 该命令执行后立即生效。

- 配置该命令前需要先使用命令ADD FILTERGP增加对应的过滤组。

- 最多可输入100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNN | DNN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~66。不区分大小写，转成小写存储，可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字和字母，不能出现连续两个“.”。<br>默认值：无<br>配置原则：无 |
| FILTERGPID | 过滤组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤组ID，可以通过LST FILTERGP命令进行查询。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFILTER]] · UPF过滤组（UPFILTER）

## 使用实例

如运营商需要特殊处理DNN为“huawei.com”条件下，实例名称为“UPF1”的UPF上的某组数据流，该数据流的相关参数与过滤组ID为1的过滤组相吻合。需要执行以下命令：

```
ADD UPFILTER: NFINSTANCENAME="UPF1", DNN="huawei.com", FILTERGPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UPFILTER.md`
