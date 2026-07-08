---
id: UNC@20.15.2@MMLCommand@LST GTPCFUNCPARA
type: MMLCommand
name: LST GTPCFUNCPARA（查询GTP-C功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCFUNCPARA
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C功能参数
status: active
---

# LST GTPCFUNCPARA（查询GTP-C功能参数）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于查询GTP-C功能参数。

## 注意事项

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令（除FILTERFAULTSW）无效，请使用命令LST GTPPUB配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCFUNCPARA]] · GTP-C功能参数（GTPCFUNCPARA）

## 使用实例

查询GTP-C功能参数：LST GTPCFUNCPARA:;

```
%%LST GTPCFUNCPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
                    V1 Echo请求发送开关  =  打开
                V1 Echo请求发送间隔(秒)  =  60
                    V2 Echo请求发送开关  =  打开
                V2 Echo请求发送间隔(秒)  =  60
                 Echo消息的重发间隔(秒)  =  3
                     Echo消息的发送次数  =  5
                           NTSR功能开关  =  关闭
                            PRN功能开关  =  关闭
                          CIOT功能开关  =  关闭
                       路径断去激活开关  =  打开
             路径断后发送心跳消息的次数  =  30
                   本端recovery更新开关  =  打开
                   对端Recovery处理开关  =  关闭
                         本端端口号模式  =  非知名端口号模式
                      UDP校验和检查开关  =  打开
             过滤故障状态的GTPC路径开关  =  打开
Bearer Resource Command使用知名源端口号  =  关闭
  Modify Bearer Command使用知名源端口号  =  关闭
  Delete Bearer Command使用知名源端口号  =  关闭
                      路径数过载门限(%)  =  85
                  路径数过载恢复门限(%)  =  80
                       发送私有信息开关  =  关闭
                       私有信息扩展域ID  =  2011
                               私有信息  =  UNC
              检查GTP扩展头类型个数上限  =  10
              检查GTP扩展头列表个数上限  =  100
              检查GTP扩展头类型长度上限  =  100
                      要求MME携带NTSR标识 = 开启
                         Recovery信元校验开关 = 关闭
               激活应答消息携带NSAPI标识 = 关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C功能参数（LST-GTPCFUNCPARA）_09651330.md`
