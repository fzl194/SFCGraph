---
id: UNC@20.15.2@MMLCommand@RMV UPFILTER
type: MMLCommand
name: RMV UPFILTER（删除UPF过滤组）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV UPFILTER（删除UPF过滤组）

## 功能

**适用NF：SMF**

该命令用于为UPF删除一个过滤组。

执行此命令后在指定DNN下的指定实例名称的UPF的指定过滤组将失效。

## 注意事项

该命令执行后立即生效。

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

删除DNN为huawei.com，UPF实例名称为"UPF1"，过滤组ID为1的记录，执行如下命令：

```
RMV UPFILTER: NFINSTANCENAME="UPF1", DNN="HUAWEI.COM", FILTERGPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UPFILTER.md`
