---
id: UNC@20.15.2@MMLCommand@LST USRBLACKLSTFUN
type: MMLCommand
name: LST USRBLACKLSTFUN（查询用户黑名单接入控制功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRBLACKLSTFUN
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入限制
- 黑名单接入限制
status: active
---

# LST USRBLACKLSTFUN（查询用户黑名单接入控制功能）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于查询用户黑名单接入限制功能开关以及拒绝原因值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRBLACKLSTFUN]] · 用户黑名单接入控制功能（USRBLACKLSTFUN）

## 使用实例

查询用户黑名单接入限制功能记录，执行如下命令：

```
%%LST USRBLACKLSTFUN:;%%
RETCODE = 0  操作成功。

查询结果如下
-------------------------
        接入限制开关  =  是
    N2模式拒绝原因值  =  15
	S1模式拒绝原因值  =  15
	IU模式拒绝原因值  =  7
	GB模式拒绝原因值  =  14
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-USRBLACKLSTFUN.md`
