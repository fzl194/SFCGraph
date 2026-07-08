---
id: UNC@20.15.2@MMLCommand@LST CAUSEMAP
type: MMLCommand
name: LST CAUSEMAP（查询原因值映射配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CAUSEMAP
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
- 移动性管理
- 原因值管理
- 原因值映射配置
status: active
---

# LST CAUSEMAP（查询原因值映射配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询原因值映射配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。<br>取值范围：1～127<br>默认值：无 |
| CAUSERANGE | 原因值范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定原因值范围。<br>取值范围：<br>- “DEFAULT(缺省)”<br>- “SPECIAL(特定)”<br>默认值：无 |
| BGCAUSE | 起始原始原因值 | 可选必选说明： 条件可选参数<br>参数含义：该参数用于指定起始原始原因值。<br>前提条件：该参数在<br>“CAUSERANGE(原因值范围)”<br>设置为<br>“SPECIAL(特定)”<br>时，才需要配置。<br>取值范围：1～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CAUSEMAP]] · 原因值映射配置（CAUSEMAP）

## 使用实例

查询原因值组标识为126，原因值范围设置为缺省的原因值映射配置：

LST CAUSEMAP: CAUSEGRPID=126, CAUSERANGE=DEFAULT;

```
%%LST CAUSEMAP: CAUSEGRPID=126, CAUSERANGE=DEFAULT;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
  原因值组标识  =  126
    原因值范围  =  缺省
起始原始原因值  =  NULL
终止原始原因值  =  NULL
    目标原因值  =  37
（结果个数 = 1）

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询原因值映射配置(LST-CAUSEMAP)_72345089.md`
