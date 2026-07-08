---
id: UNC@20.15.2@MMLCommand@LST CHRMGMTPARA
type: MMLCommand
name: LST CHRMGMTPARA（查询关键流程CHR上报管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHRMGMTPARA
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- CHR管理
- CHR上报管理
status: active
---

# LST CHRMGMTPARA（查询关键流程CHR上报管理参数）

## 功能

**适用NF：AMF、SMF**

该命令用于查询关键流程CHR上报管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHRMGMTPARA]] · 关键流程CHR上报管理参数（CHRMGMTPARA）

## 使用实例

查询关键流程CHR上报管理参数。

```
%%LST CHRMGMTPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  失败时允许上报CHR的流程  =  NF Discovery
        允许上报CHR的机制  =  NF Cache Update&Link Change
流程触发的CHR上报速率阈值  =  10
机制触发的CHR上报速率阈值  =  10
服务发现上报CHR的抑制时间  =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询关键流程CHR上报管理参数（LST-CHRMGMTPARA）_28868621.md`
