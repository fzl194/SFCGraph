---
id: UNC@20.15.2@MMLCommand@LST TAICIOT
type: MMLCommand
name: LST TAICIOT（查询CIoT能力配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TAICIOT
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- CIoT能力配置
status: active
---

# LST TAICIOT（查询CIoT能力配置）

## 功能

**适用网元：MME**

该命令用于查询TAI下所有eNodeB的蜂窝物联网（CIoT）能力。

## 注意事项

不输入任何参数则表示查询所有信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAI | TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的跟踪区标识。<br>数据来源：全网规划<br>取值范围：9～10位的字符串。<br>默认值：无 |

## 操作的配置对象

- [CIoT能力配置（TAICIOT）](configobject/UNC/20.15.2/TAICIOT.md)

## 使用实例

查看系统中所有eNodeB的CIoT能力配置记录：

LST TAICIOT:;

```
%%LST TAICIOT:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------
             起始TAI  =  308015101
             终止TAI  =  308015201
窄带数据传输能力指示  =  支持CP CIoT
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CIoT能力配置(LST-TAICIOT)_72225461.md`
