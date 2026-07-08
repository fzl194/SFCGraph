---
id: UNC@20.15.2@MMLCommand@LST DNNSMARTPLCY
type: MMLCommand
name: LST DNNSMARTPLCY（查询DNN智能分流配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNNSMARTPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- DNN智能分流管理
- DNN智能分流开启策略
status: active
---

# LST DNNSMARTPLCY（查询DNN智能分流配置）

## 功能

**适用NF：AMF**

该命令用于查询PDU会话创建使用的DNN智能分流配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户会话创建使用的DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNNSMARTPLCY]] · DNN智能分流配置（DNNSMARTPLCY）

## 使用实例

查询DNN“huawei.com”智能分流配置，执行如下命令：

```
%%LST DNNSMARTPLCY: DNN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
------------------------
              DNN  =  huawei.com
是否支持专用SMF选择  =  Yes
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNNSMARTPLCY.md`
