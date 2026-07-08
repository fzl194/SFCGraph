---
id: UNC@20.15.2@MMLCommand@LST GMLCAU
type: MMLCommand
name: LST GMLCAU（查询GMLC权限配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GMLCAU
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
- GMLC权限配置
status: active
---

# LST GMLCAU（查询GMLC权限配置）

## 功能

**适用网元：MME**

此命令用于查询GMLC权限配置。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCID | GMLC 标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的GMLC标识。<br>取值范围：0～639<br>默认值 ：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLCAU]] · GMLC权限配置（GMLCAU）

## 使用实例

查询GMLCAU参数设置：

LST GMLCAU:;

```
%%LST GMLCAU:;%%
RETCODE = 0  操作成功。

 查询结果如下
--------------
 GMLC 标识  支持的客户端类型  支持的LCS业务类型

 1          紧急业务          2                
 1          增值业务          3                
 2          增值业务          44               
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GMLCAU.md`
