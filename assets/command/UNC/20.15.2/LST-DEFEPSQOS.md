---
id: UNC@20.15.2@MMLCommand@LST DEFEPSQOS
type: MMLCommand
name: LST DEFEPSQOS（查询EPS缺省QoS参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DEFEPSQOS
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- 全局EPS QoS纠错
status: active
---

# LST DEFEPSQOS（查询EPS缺省QoS参数）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于显示系统配置的EPS缺省QoS参数取值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEFEPSQOS]] · EPS缺省QoS参数（DEFEPSQOS）

## 使用实例

显示系统配置的EPS缺省QoS参数取值：

```
%%LST DEFEPSQOS:;%%
RETCODE = 0  操作成功

缺省的EPS QoS配置信息
---------------------
                  QCI值  =  5
                  ARP值  =  3
下行保证带宽(千比特/秒)  =  400
上行保证带宽(千比特/秒)  =  400
下行最大带宽(千比特/秒)  =  500
上行最大带宽(千比特/秒)  =  500
下行APN AMBR(千比特/秒)  =  2000
上行APN AMBR(千比特/秒)  =  2000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询EPS缺省QoS参数（LST-DEFEPSQOS）_09653169.md`
