---
id: UNC@20.15.2@MMLCommand@LST S1CMPT
type: MMLCommand
name: LST S1CMPT（查询S1接口兼容性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1CMPT
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1接口兼容性
status: active
---

# LST S1CMPT（查询S1接口兼容性）

## 功能

**适用网元：MME**

该命令用于查询S1接口兼容性。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1CMPT]] · S1接口兼容性（S1CMPT）

## 使用实例

查询S1接口兼容配置，运行如下命令：

LST S1CMPT:;

```
%%LST S1CMPT:;%%
RETCODE = 0  操作成功

操作结果如下
------------
                  是否支持Register LAI信元  =  不支持
                       发送所有MME服务PLMN  =  否
                  eNodeB是否支持祖冲之算法  =  是
                  是否携带Time to Wait信元  =  否
         NAS transport消息是否携带SPID信元  =  是
          NAS TRANSPORT消息是否携带HRL信元  =  是
                     Masked IMEISV发送范围  =  所有eNodeB
                Next Paging Area Scope开关  =  否
                是否携带NR Restriction信元  =  是
   是否携带NR UE Security Capabilities信元  =  是
                  是否携带Security Context  =  是
         是否携带NR Restriction in 5GS信元  =  否
是否携带Core Network Type Restrictions信元  =  否
                     是否支持S1 Part Reset  =  不支持
                 是否携带GUAMI映射的GUMMEI  =  否
                   是否携带GUMMEI Type信元  =  否
      是否携带Warning Area Coordinates信元  =  否
  是否携带Extended UE Identity Index Value  =  否
是否携带Management Based MDT PLMN List信元  =  否
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-S1CMPT.md`
