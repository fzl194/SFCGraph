---
id: UNC@20.15.2@MMLCommand@LST HTRIMSICFG
type: MMLCommand
name: LST HTRIMSICFG（查询HTR号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTRIMSICFG
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
- 配置局向关联号段
status: active
---

# LST HTRIMSICFG（查询HTR号段）

## 功能

**适用网元：SGSN**

该命令用于查询一个HTR局向的具体IMSI号段。只有当HTROFC配置表中 “HTR局向索引” 对应的 “局向流控开关” 为 “YES” 时，本命令所配置的各个IMSI号段才进行流控，可执行 [**LST HTROFC**](../配置局向/查询HTR局向(LST HTROFC)_26305964.md) 进行查看。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [HTR号段（HTRIMSICFG）](configobject/UNC/20.15.2/HTRIMSICFG.md)

## 使用实例

查询HTR参数：

LST HTRIMSICFG:;

```
%%LST HTRIMSICFG:;%%
RETCODE = 0 操作成功。

输出结果如下
-------------------------
      IMSI前缀  =  123030001
   HTR局向索引  =  0
      (结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTR号段(LST-HTRIMSICFG)_72225831.md`
