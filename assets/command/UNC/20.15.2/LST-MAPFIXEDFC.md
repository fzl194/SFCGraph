---
id: UNC@20.15.2@MMLCommand@LST MAPFIXEDFC
type: MMLCommand
name: LST MAPFIXEDFC（查询SMS的MAP接口固定速率流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MAPFIXEDFC
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 接口流控
- MAP接口流控
status: active
---

# LST MAPFIXEDFC（查询SMS的MAP接口固定速率流控）

## 功能

**适用NF：SMSF**

该命令用于查询短消息MAP接口固定速率配置参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [SMS的MAP接口固定速率流控（MAPFIXEDFC）](configobject/UNC/20.15.2/MAPFIXEDFC.md)

## 使用实例

查询短消息MAP接口固定速率配置参数，执行如下命令：

```
LST MAPFIXEDFC:;
%%LST MAPFIXEDFC:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
            流控开关  =  开启
MT消息流控速率(个/秒) =  10001
        流控处理方式  =  失败响应
      流控响应原因值  =  资源限制
        阈值计算策略  =  整系统
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMS的MAP接口固定速率流控（LST-MAPFIXEDFC）_36063248.md`
