---
id: UNC@20.15.2@MMLCommand@LST APNACCESSCTRL
type: MMLCommand
name: LST APNACCESSCTRL（查询APN访问控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNACCESSCTRL
command_category: 查询类
applicable_nf:
- SMF
- GGSN
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 基于APN的接入属性控制
status: active
---

# LST APNACCESSCTRL（查询APN访问控制参数）

## 功能

**适用NF：SMF、GGSN、SGW-C、PGW-C**

该命令用于查询APN访问控制策略相关参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNACCESSCTRL]] · APN访问控制参数（APNACCESSCTRL）

## 使用实例

该命令支持全局查询。当需要查询指定APN名称为huawei.com的访问控制参数信息时，可以执行如下命令

```
%%LST APNACCESSCTRL: APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
                               APN名称  =  huawei.com
      SMF/PGW/GGSN拜访用户接入功能开关  =  使能
                   最大带宽(兆比特/秒)  =  0
               最大保证带宽(兆比特/秒)  =  0
                           最大PDP数目  =  0
              不携带MSISDN用户激活策略  =  使能
       Apn-restriction本地校验功能开关  =  使能
               Apn-restriction功能开关  =  不使能
                 Apn-restriction最大值  =  0
              用户选择模式检查功能开关  =  不使能
           SMF用户选择模式检查功能开关  =  不使能
                 Ms提供APN用户激活策略  =  不使能
         Ms/Network提供APN用户激活策略  =  使能
            Network提供APN用户激活策略  =  不使能
     SMF/SGW上控制漫游用户接入功能开关  =  使能
     SMF/SGW上控制拜访用户接入功能开关  =  使能
SMF/PGW/GGSN上控制漫游用户接入功能开关  =  使能
                不携带IMSI用户激活策略  =  继承全局
                   APN跨省漫游限制开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNACCESSCTRL.md`
