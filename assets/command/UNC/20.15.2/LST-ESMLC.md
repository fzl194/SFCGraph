---
id: UNC@20.15.2@MMLCommand@LST ESMLC
type: MMLCommand
name: LST ESMLC（查询E-SMLC配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ESMLC
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- E-SMLC配置
status: active
---

# LST ESMLC（查询E-SMLC配置）

## 功能

**适用网元：MME**

此命令用于查询E-SMLC配置。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ESMLCID | E-SMLC 标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的E-SMLC标识。<br>取值范围：0～255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ESMLC]] · E-SMLC配置（ESMLC）

## 使用实例

查询E-SMLC参数设置：

LST ESMLC:;

```
%%LST ESMLC:;%%
RETCODE = 0  操作成功。

查询结果如下
-------------------------
 E-SMLC 标识  优先级  E-SMLC名称  是否携带RAT Type信元

 1            2       ESMLC1      否
 2            3       ESMLC2      否  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ESMLC.md`
