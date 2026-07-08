---
id: UNC@20.15.2@MMLCommand@LST SGSLKS
type: MMLCommand
name: LST SGSLKS（查询SGs链路集）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSLKS
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路集管理
status: active
---

# LST SGSLKS（查询SGs链路集）

## 功能

**适用网元：MME**

此命令用于查询SGs链路集。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：可选参数<br>参数含义：待查询链路集的索引。<br>取值范围：0~255<br>默认值：无 |
| LSN | 链路集名 | 可选必选说明：可选参数<br>参数含义：待查询链路集的名称。<br>取值范围：1~50位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGSLKS]] · SGs链路集（SGSLKS）

## 使用实例

查询所有链路集：

LST SGSLKS:;

```
%%LST SGSLKS:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
 链路集索引  VLR号   链路集名

 0           11808   VLR8    
 1           11809   VLR9    
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGs链路集(LST-SGSLKS)_26305250.md`
