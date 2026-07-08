---
id: UNC@20.15.2@MMLCommand@LST NCGSOFTPARAOFBIT
type: MMLCommand
name: LST NCGSOFTPARAOFBIT（查询NCG软件参数比特位）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NCGSOFTPARAOFBIT
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软件参数管理
status: active
---

# LST NCGSOFTPARAOFBIT（查询NCG软件参数比特位）

## 功能

**适用NF：NCG**

该命令用于查询NCG软件参数，查询结果以二进制形式输出。同时，该命令也支持查询指定软件参数中某个比特位的值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- Dw（双字）<br>- Byte（字节）<br>默认值：无<br>配置原则：无 |
| DWORDNUM | Dword索引 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件可选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |
| POSITION | 比特位 | 可选必选说明：可选参数<br>参数含义：该参数表示软件参数比特位的位置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NCGSOFTPARAOFBIT]] · NCG软件参数比特位（NCGSOFTPARAOFBIT）

## 使用实例

查询当前软参记录索引为1，比特位为1的双字类型软参的设置情况：

```
LST NCGSOFTPARAOFBIT: DT=Dw, DWORDNUM=1,POSITION=1;
RETCODE = 0  操作成功

结果如下
--------
    数据类型  =  双字
软参记录索引  =  1
      比特位  =  1
  软参记录值  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NCGSOFTPARAOFBIT.md`
