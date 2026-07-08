---
id: UNC@20.15.2@MMLCommand@LST NGIPAREACTRL
type: MMLCommand
name: LST NGIPAREACTRL（查询基于位置的地址分配控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGIPAREACTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- IP细分管理
- 5G地址细分控制参数
status: active
---

# LST NGIPAREACTRL（查询基于位置的地址分配控制参数）

## 功能

**适用NF：AMF**

该命令用于查询“基于位置的地址分配”的策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGIPAREACTRL]] · 基于位置的地址分配控制参数（NGIPAREACTRL）

## 使用实例

查询“基于位置的地址分配”的策略。

```
%%LST NGIPAREACTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
        用户下线开关  =  开启
        去注册原因值  =  15
语音会话延迟下线开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGIPAREACTRL.md`
