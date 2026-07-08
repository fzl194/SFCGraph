---
id: UNC@20.15.2@MMLCommand@LST HNOINFO
type: MMLCommand
name: LST HNOINFO（查询归属网络信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HNOINFO
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- 归属网络信息管理
status: active
---

# LST HNOINFO（查询归属网络信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询归属网络信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商标识<br>取值范围：0～64，128～254<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HNOINFO]] · 归属网络信息（HNOINFO）

## 使用实例

查看所有的HNOINFO:

LST HNOINFO:;

```
%%LST HNOINFO:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
     运营商标识  =  0
     本局SGSN号  =  123
   本地实体索引  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HNOINFO.md`
