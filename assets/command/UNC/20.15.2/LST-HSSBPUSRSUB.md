---
id: UNC@20.15.2@MMLCommand@LST HSSBPUSRSUB
type: MMLCommand
name: LST HSSBPUSRSUB（查询HSS BYPASS最小用户签约数据配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HSSBPUSRSUB
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
- 可靠性管理
- HSS BYPASS最小签约数据配置管理
status: active
---

# LST HSSBPUSRSUB（查询HSS BYPASS最小用户签约数据配置）

## 功能

**适用网元：MME**

此命令用于查询HSS BYPASS最小用户签约数据配置。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置HSS BYPASS最小签约数据集的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>配置原则：对于指定的用户（群），HSS Bypass最小签约数据集的匹配优先级从高到低依次为：<br>“IMSI_PREFIX(指定IMSI前缀)”<br>，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：本端规划<br>取值范围：5～15位十进制数字字符串<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HSSBPUSRSUB]] · HSS BYPASS最小用户签约数据配置（HSSBPUSRSUB）

## 使用实例

查询HSS BYPASS最小用户签约数据配置，可以用如下命令：

LST HSSBPUSRSUB:;

```
%%LST HSSBPUSRSUB:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
          用户范围  =  IMSI前缀
          IMSI前缀  =  12345678
            STN-SR  =  123
      网络接入模式  =  PS和CS域
运营商闭锁分组业务  =  禁止所有用户
         APN群组ID  =  1

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HSS-BYPASS最小用户签约数据配置-(LST-HSSBPUSRSUB)_63849436.md`
