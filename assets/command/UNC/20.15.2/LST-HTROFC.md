---
id: UNC@20.15.2@MMLCommand@LST HTROFC
type: MMLCommand
name: LST HTROFC（查询HTR局向）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTROFC
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- HTR流控局向管理
- Gr HTR流控局向管理
- 配置局向
status: active
---

# LST HTROFC（查询HTR局向）

## 功能

**适用网元：SGSN**

该命令用于查询HTR局向配置信息。在GT转发的组网配置下，只有STP对SGSN逻辑上可见，HLR目的实体对SGSN是不可见的，所以需要用户手动配置具体的HTR局向进行区分，以保证准确的流控对象，避免误控。详细功能说明可参见 [**SET HTR**](../流控功能管理/设置HTR功能(SET HTR)_72345749.md) 。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTROFCINDEX | HTR局向索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTR局向的索引。<br>取值范围：0~9<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTROFC]] · HTR局向（HTROFC）

## 使用实例

查询HTR参数：

LST HTROFC:;

```
%%LST HTROFC:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
 HTR局向索引  HTR局向名称  局向流控开关
 1            1            否                        
 0            123          否                        
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTR局向(LST-HTROFC)_26305964.md`
