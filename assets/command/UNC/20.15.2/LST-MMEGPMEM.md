---
id: UNC@20.15.2@MMLCommand@LST MMEGPMEM
type: MMLCommand
name: LST MMEGPMEM（查询MME群组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMEGPMEM
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MME群组管理
- MME群组成员配置
status: active
---

# LST MMEGPMEM（查询MME群组成员）

## 功能

**适用网元：MME**

该命令用于显示MME群组成员。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEGPIDX | MME群组索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME群组索引。<br>数据来源：全网规划<br>取值范围：0~63<br>默认值：无 |
| MMEC | MME编码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME编码。<br>数据来源：全网规划<br>取值范围：2位16进制编码<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MMEGPMEM]] · MME群组成员（MMEGPMEM）

## 使用实例

查询MME群组成员所有配置

LST MMEGPMEM:;

```
%%LST MMEGPMEM:;%%
RETCODE = 0  操作成功。

查询结果如下
------------------------
MME群组索引  =  1
    MME编码  =  11
   设备能力  =  255
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MMEGPMEM.md`
