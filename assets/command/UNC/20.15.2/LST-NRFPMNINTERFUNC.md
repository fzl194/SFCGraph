---
id: UNC@20.15.2@MMLCommand@LST NRFPMNINTERFUNC
type: MMLCommand
name: LST NRFPMNINTERFUNC（查询基于对端PLMN国际漫游功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFPMNINTERFUNC
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# LST NRFPMNINTERFUNC（查询基于对端PLMN国际漫游功能参数）

## 功能

**适用NF：NRF**

此命令用于查询基于对端PLMN的国际漫游功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示指定对端PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示指定对端PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPMNINTERFUNC]] · 基于对端PLMN国际漫游功能参数（NRFPMNINTERFUNC）

## 使用实例

查询基于对端PLMN国际漫游功能参数：NA

```
%%LST NRFPMNINTERFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                  移动国家码  =  233
                    移动网号  =  13
本NRF是否是国际漫游关口局NRF  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFPMNINTERFUNC.md`
