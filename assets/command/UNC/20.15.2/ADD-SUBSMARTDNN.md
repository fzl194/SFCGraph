---
id: UNC@20.15.2@MMLCommand@ADD SUBSMARTDNN
type: MMLCommand
name: ADD SUBSMARTDNN（增加智能分流DNN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SUBSMARTDNN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- DNN智能分流管理
- 智能分流DNN管理
status: active
---

# ADD SUBSMARTDNN（增加智能分流DNN）

## 功能

**适用NF：AMF**

该命令用于增加智能分流DNN，当用户签约DNN与该DNN完全匹配时，系统标记用户为智能分流用户。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 智能分流DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定智能分流的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [智能分流DNN（SUBSMARTDNN）](configobject/UNC/20.15.2/SUBSMARTDNN.md)

## 使用实例

增加一条签约智能分流DNN，执行如下命令：

```
ADD SUBSMARTDNN: DNN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加智能分流DNN（ADD-SUBSMARTDNN）_39800053.md`
