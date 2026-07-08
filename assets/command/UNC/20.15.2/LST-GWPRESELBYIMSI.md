---
id: UNC@20.15.2@MMLCommand@LST GWPRESELBYIMSI
type: MMLCommand
name: LST GWPRESELBYIMSI（查询指定用户优选网关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GWPRESELBYIMSI
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- 网关优选
- 指定用户优选网关
status: active
---

# LST GWPRESELBYIMSI（查询指定用户优选网关）

## 功能

**适用网元：MME**

该命令用于查询指定用户优选网关记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户IMSI。<br>数据来源：整网规划<br>取值范围：14~15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWPRESELBYIMSI]] · 指定用户优选网关（GWPRESELBYIMSI）

## 使用实例

1. 不输入查询条件，查询全部指定用户优选网关记录：
  LST GWPRESELBYIMSI:;
  ```
  %%LST GWPRESELBYIMSI:;%%
  RETCODE = 0  操作成功。

  查询结果如下
  ------------------------
  IMSI             RAT TYPE                 SGW主机名                                    GGSN主机名               

  123030000100001  Gb MODE&Iu MODE&S1 MODE  TOPON.SGW.SGW1.EPC.MNC03.MCC123.3GPPNETWORK.ORG  INTERNET.MNC003.MCC123.GPRS  
  123030000100002  Gb MODE&Iu MODE&S1 MODE  TOPON.SGW.SGW1.EPC.MNC03.MCC123.3GPPNETWORK.ORG  INTERNET.MNC003.MCC123.GPRS  
  (结果个数 = 2)

  ---    END
  ```
2. 查询用户IMSI为"123030000100001"的指定用户优选网关记录：
  LST GWPRESELBYIMSI: IMSI="123030000100001";
  ```
  %%LST GWPRESELBYIMSI: IMSI="123030000100001";%%
  RETCODE = 0  操作成功。

  查询结果如下
  ------------------------
            IMSI  =  123030000100001
        RAT TYPE  =  Gb MODE&Iu MODE&S1 MODE
       SGW主机名  =  TOPON.SGW.SGW1.EPC.MNC03.MCC123.3GPPNETWORK.ORG
      GGSN主机名  =  INTERNET.MNC003.MCC123.GPRS
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定用户优选网关（LST-GWPRESELBYIMSI）_59644410.md`
