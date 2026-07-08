---
id: UNC@20.15.2@MMLCommand@LST MNCLEN
type: MMLCommand
name: LST MNCLEN（查询MNC长度信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MNCLEN
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- MNC长度
status: active
---

# LST MNCLEN（查询MNC长度信息）

## 功能

**适用NF：SMF**

该命令用于查看MCC号对应的MNC长度。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。取值范围000～999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MNCLEN]] · MNC长度信息（MNCLEN）

## 使用实例

查看当前UNC所属的MCC的MNC长度：

```
%%LST MNCLEN:;%%
RETCODE = 0  操作成功

结果如下
--------
      移动国家码  =  233
对应MCC的MNC长度  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MNCLEN.md`
