---
id: UNC@20.15.2@MMLCommand@LST RCFIXEDFC
type: MMLCommand
name: LST RCFIXEDFC（查询注册中心固定速率流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RCFIXEDFC
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMSF固定速率流控
status: active
---

# LST RCFIXEDFC（查询注册中心固定速率流控）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF/VLR向注册中心发送请求的固定速率流控。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RCFIXEDFC]] · 注册中心固定速率流控（RCFIXEDFC）

## 使用实例

运营商希望查询SMSF/VLR向注册中心发送请求的固定速率流控参数，执行如下命令：

```
LST RCFIXEDFC:;
%%LST RCFIXEDFC:;%%
RETCODE = 0  操作成功

结果如下：
----------
            SMSF/VLR向注册中心发送注册请求的固定速率流控开关  =  开启
            SMSF/VLR向注册中心发送查询请求的固定速率流控开关  =  开启			
SMSF/VLR向注册中心发送注册请求的固定速率流控的起控阈值(个/秒) =  10000 
SMSF/VLR向注册中心发送查询请求的固定速率流控的起控阈值(个/秒) =  10000
                                                阈值计算策略  =  整系统
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RCFIXEDFC.md`
