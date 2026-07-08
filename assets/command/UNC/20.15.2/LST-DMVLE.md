---
id: UNC@20.15.2@MMLCommand@LST DMVLE
type: MMLCommand
name: LST DMVLE（查询Diameter虚拟本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMVLE
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter虚拟本地实体
status: active
---

# LST DMVLE（查询Diameter虚拟本地实体）

## 功能

**适用网元：MME**

该命令用于查询Diameter虚拟本地实体信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定虚拟本地实体的索引，唯一标识一个本地实体。<br>取值范围：32~63<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMVLE]] · Diameter虚拟本地实体（DMVLE）

## 使用实例

查询单个Diameter虚拟本地实体信息：

LST DMVLE: LOINDEX=32;

```
%%LST DMVLE: LOINDEX=32;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
  本地实体索引  =  32
本地实体主机名  =  example.com
  本地实体域名  =  exaple.com
        产品名  =  MME
    本地实体名  =  DMVLE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter虚拟本地实体(LST-DMVLE)_72345897.md`
