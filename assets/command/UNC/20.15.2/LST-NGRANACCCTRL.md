---
id: UNC@20.15.2@MMLCommand@LST NGRANACCCTRL
type: MMLCommand
name: LST NGRANACCCTRL（查询5G基站接入控制策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGRANACCCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN接入管理控制
status: active
---

# LST NGRANACCCTRL（查询5G基站接入控制策略）

## 功能

**适用NF：AMF**

该命令用于查询5G基站接入控制策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGRANACCCTRL]] · 5G基站接入控制策略（NGRANACCCTRL）

## 使用实例

查询5G基站接入控制策略，执行如下命令：

```
%%LST NGRANACCCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
      基于位置区基站接入限制开关  =  开启
                  跟踪区群组标识  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGRANACCCTRL.md`
