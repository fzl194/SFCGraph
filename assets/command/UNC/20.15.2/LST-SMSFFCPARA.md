---
id: UNC@20.15.2@MMLCommand@LST SMSFFCPARA
type: MMLCommand
name: LST SMSFFCPARA（查询SMSF自保流控的参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFFCPARA
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 接口流控
- SMSF自保流控
status: active
---

# LST SMSFFCPARA（查询SMSF自保流控的参数）

## 功能

**适用NF：SMSF**

该命令用于查询流控等级对应的流控响应。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFFCPARA]] · SMSF自保流控的参数（SMSFFCPARA）

## 使用实例

运营商想要查询流控等级对应的流控响应类型，执行如下命令：

```
LST SMSFFCPARA:;
%%LST SMSFFCPARA:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
        流控开关  =  开启
轻度过载流控响应  =  服务不可用
中度过载流控响应  =  服务不可用
重度过载流控响应  =  服务不可用
 MAP接口流控响应  =  资源限制
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSFFCPARA.md`
