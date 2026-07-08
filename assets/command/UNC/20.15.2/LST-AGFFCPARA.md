---
id: UNC@20.15.2@MMLCommand@LST AGFFCPARA
type: MMLCommand
name: LST AGFFCPARA（查询流控等级对应的流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AGFFCPARA
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- AGF流控参数信息
status: active
---

# LST AGFFCPARA（查询流控等级对应的流控参数）

## 功能

**适用NF：NCG**

该命令用于查询流控等级对应的流控参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCLEVEL | 流控等级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示CPU过载程度的分级。<br>数据来源：本端规划<br>取值范围：<br>- “LOW（轻度过载）”：根据LOW选择FCL<br>- “MEDIUM（中度过载）”：根据MEDIUM选择FCL<br>- “HIGH（重度过载）”：根据HIGH选择FCL<br>默认值：无<br>配置原则：<br>LOW（轻度过载）：轻度过载对应的CPU阈值范围为大于等于75%、小于80%。<br>MEDIUM（中度过载）：中度过载对应的CPU阈值范围为大于等于80%、小于85%。<br>HIGH（重度过载）：重度过载对应的CPU阈值范围为大于等于85%、小于100%。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AGFFCPARA]] · 流控等级对应的流控参数（AGFFCPARA）

## 使用实例

查询流控等级为LOW的流控响应参数：

```
LST AGFFCPARA: FCLEVEL=LOW;
RETCODE = 0  操作成功

结果如下
--------
流控等级  =  轻度过载
流控响应  =  无响应
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流控等级对应的流控参数（LST-AGFFCPARA）_45110914.md`
