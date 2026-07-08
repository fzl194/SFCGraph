---
id: UNC@20.15.2@MMLCommand@LST NRFLOGFCPARA
type: MMLCommand
name: LST NRFLOGFCPARA（查询NRF日志流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFLOGFCPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF维测管理
status: active
---

# LST NRFLOGFCPARA（查询NRF日志流控参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF日志流控参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：可选参数<br>参数含义：该参数表示NRF提供的服务类型。<br>数据来源：本端规划<br>取值范围：<br>- DISC（DISC）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFLOGFCPARA]] · NRF日志流控参数（NRFLOGFCPARA）

## 使用实例

通过以下命令查询NRF日志流控参数：

```
%%LST NRFLOGFCPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
        服务类型  =  DISC
        流控开关  =  打开
    流控周期(秒)  =  10
最大打印条数(个)  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFLOGFCPARA.md`
