---
id: UNC@20.15.2@MMLCommand@LST HLRFIXEDFC
type: MMLCommand
name: LST HLRFIXEDFC（查询VLR向HLR发送请求的固定速率流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HLRFIXEDFC
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- VLR固定速率流控
status: active
---

# LST HLRFIXEDFC（查询VLR向HLR发送请求的固定速率流控）

## 功能

**适用NF：SMSF**

该命令用于查询VLR向HLR发送请求的固定速率流控。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HLRFIXEDFC]] · VLR向HLR发送请求的固定速率流控（HLRFIXEDFC）

## 使用实例

运营商希望查询VLR向HLR发送请求的固定速率流控参数，执行如下命令：

```
LST HLRFIXEDFC:;
%%LST HLRFIXEDFC:;%%
RETCODE = 0  操作成功

结果如下：
--------------
            VLR向HLR发送位置更新请求的固定速率流控开关  =  开启
    VLR向HLR发送位置更新请求的固定速率的起控阈值(个/秒) =  10000
	                                      阈值计算策略  =  整系统
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR向HLR发送请求的固定速率流控（LST-HLRFIXEDFC）_53641450.md`
