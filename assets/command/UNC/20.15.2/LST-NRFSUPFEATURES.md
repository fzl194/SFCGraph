---
id: UNC@20.15.2@MMLCommand@LST NRFSUPFEATURES
type: MMLCommand
name: LST NRFSUPFEATURES（查询NRF服务能力参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSUPFEATURES
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF服务能力参数管理
status: active
---

# LST NRFSUPFEATURES（查询NRF服务能力参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF网元特定服务是否携带能力参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：可选参数<br>参数含义：该参数表示NRF服务类型。选择NFM表示设置NF管理类服务中的订阅功能支持的能力，选择DISC表示设置NF服务发现功能支持的能力。<br>数据来源：本端规划<br>取值范围：<br>- DISC（DISC）<br>- NFM（NFM）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSUPFEATURES]] · NRF服务能力参数（NRFSUPFEATURES）

## 使用实例

查询NRF服务是否携带能力参数。

```
LST NRFSUPFEATURES:;
%%LST NRFSUPFEATURES:;%%
RETCODE = 0  操作成功

结果如下
------------------------
服务类型    能力参数携带开关                                

NFM         打开                                
DISC        关闭                            
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF服务能力参数（LST-NRFSUPFEATURES）_08839360.md`
