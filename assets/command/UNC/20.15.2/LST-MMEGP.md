---
id: UNC@20.15.2@MMLCommand@LST MMEGP
type: MMLCommand
name: LST MMEGP（显示MME群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMEGP
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MME群组管理
- MME群组配置
status: active
---

# LST MMEGP（显示MME群组）

## 功能

**适用网元：MME**

该命令用于显示MME群组。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEGPIDX | MME群组索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME群组索引。<br>数据来源：全网规划<br>取值范围：0～63<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家码<br>数据来源：全网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：位数为2或3的十进制数<br>默认值：无 |
| MMEGI | MME组识别码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME组识别码。<br>数据来源：全网规划<br>取值范围：4位16进制编码<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MMEGP]] · MME群组（MMEGP）

## 使用实例

查询所有MME群组配置记录

LST MMEGP:;

```
%%LST MMEGP:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
MME群组索引  =  1
 移动国家码  =  123
   移动网号  =  001
MME组识别码  =  0001
   描述信息  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MMEGP.md`
